import Foundation
import PDFKit

struct PageRecord: Codable {
    let page: Int
    let text: String
    let annotations: [String]
}
struct PDFRecord: Codable {
    let source: String
    let pageCount: Int
    let pages: [PageRecord]
}
let input = CommandLine.arguments[1]
let output = CommandLine.arguments[2]
guard let pdf = PDFDocument(url: URL(fileURLWithPath: input)) else {
    fatalError("Could not open input PDF")
}
let pages = (0..<pdf.pageCount).compactMap { i -> PageRecord? in
    guard let p = pdf.page(at: i) else { return nil }
    let annotations = p.annotations.compactMap { a -> String? in
        guard let text = a.contents, !text.isEmpty else { return nil }
        return text
    }
    return PageRecord(page: i + 1, text: p.string ?? "", annotations: annotations)
}
let record = PDFRecord(source: input, pageCount: pdf.pageCount, pages: pages)
let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
try encoder.encode(record).write(to: URL(fileURLWithPath: output))
print("Extracted \(pdf.pageCount) pages to \(output)")
